#!/usr/bin/env node
import { execSync } from 'child_process'
import { mkdirSync, cpSync, rmSync, existsSync, writeFileSync } from 'fs'
import { join } from 'path'

const branch = process.env.BRANCH_NAME || process.env.GITHUB_REF_NAME || 'main'
const baseOutputDir = 'dist-versioned'
const outputDir = branch === 'main' ? baseOutputDir : join(baseOutputDir, branch)

console.log(`Building docs for branch: ${branch}`)
console.log(`Output directory: ${outputDir}`)

try {
  // Set environment variable for config
  process.env.BRANCH_NAME = branch

  // Build the docs
  execSync('pnpm run docs:build', { stdio: 'inherit' })

  // Create base output directory
  mkdirSync(baseOutputDir, { recursive: true })

  // For main branch, preserve existing version directories but update root
  if (branch === 'main') {
    // Copy built files to root, but preserve existing subdirectories
    const tempDir = 'temp-main-build'
    if (existsSync(tempDir)) {
      rmSync(tempDir, { recursive: true, force: true })
    }
    cpSync('docs/.vitepress/dist', tempDir, { recursive: true })

    // Copy everything except directories that look like version names
    const builtFiles = ['index.html', 'assets', 'basic-rules', 'master-data',
                       'electronic-billing', 'accounting-management', 'purchase-management',
                       'return-management', 'distribution-management', 'material-management',
                       'production-management', 'pdv-management', 'human-management',
                       'customer-relationship-management', 'balance-management',
                       'sales-management', 'financial-management', 'asset-management',
                       'frequently-asked-questions', 'verticals', 'devices', 'favicon.ico']

    for (const file of builtFiles) {
      const sourcePath = join(tempDir, file)
      const destPath = join(baseOutputDir, file)
      if (existsSync(sourcePath)) {
        if (existsSync(destPath)) {
          rmSync(destPath, { recursive: true, force: true })
        }
        cpSync(sourcePath, destPath, { recursive: true })
      }
    }

    // Clean up temp directory
    rmSync(tempDir, { recursive: true, force: true })
  } else {
    // For other branches, just copy to their specific directory
    if (existsSync(outputDir)) {
      rmSync(outputDir, { recursive: true, force: true })
    }
    mkdirSync(outputDir, { recursive: true })
    cpSync('docs/.vitepress/dist', outputDir, { recursive: true })
  }

  // Create/update a versions index file
  const versionsFile = join(baseOutputDir, 'versions.json')
  let versions = []
  if (existsSync(versionsFile)) {
    try {
      versions = JSON.parse(require('fs').readFileSync(versionsFile, 'utf8'))
    } catch (e) {
      versions = []
    }
  }

  if (!versions.includes(branch)) {
    versions.push(branch)
    writeFileSync(versionsFile, JSON.stringify(versions.sort(), null, 2))
  }

  console.log(`Docs built successfully for branch ${branch}`)
  console.log(`Available versions: ${versions.join(', ')}`)

} catch (error) {
  console.error('Build failed:', error.message)
  process.exit(1)
}