---
id: google-sheets
title: Google Sheets Tools
sidebar_position: 7
---

# Google Sheets Tools

All tools for reading and writing Google Sheets data.

## Account & Discovery Tools

| Tool | Operation | Description |
|------|-----------|-------------|
| `list-google-sheets-accounts` | Read | List connected Google accounts |
| `list-google-sheets-spreadsheets` | Read | List all accessible spreadsheets |

## Spreadsheet Tools

| Tool | Operation | Description |
|------|-----------|-------------|
| `get-google-sheets-spreadsheet` | Read | Get all data from a spreadsheet |
| `get-google-sheets-spreadsheet-info` | Read | Get spreadsheet metadata (sheets, dimensions) |
| `list-google-sheets-worksheets` | Read | List worksheets within a spreadsheet |
| `create-google-sheets-spreadsheet` | Write | Create a new spreadsheet |

## Row & Cell Tools

| Tool | Operation | Description |
|------|-----------|-------------|
| `get-google-sheets-values` | Read | Get values from a range |
| `read-google-sheets-rows` | Read | Read all rows from a worksheet |
| `get-google-sheets-cell` | Read | Get a single cell value |
| `find-google-sheets-row` | Read | Find the first row matching a condition |
| `find-google-sheets-rows` | Read | Find all rows matching a condition |
| `add-google-sheets-row` | Write | Append a new row |
| `add-google-sheets-rows` | Write | Append multiple rows at once |
| `update-google-sheets-row` | Write | Update an existing row |
| `update-google-sheets-cell` | Write | Update a single cell |
| `delete-google-sheets-rows` | Delete | Delete specific rows |
| `clear-google-sheets-rows` | Write | Clear row content without deleting the rows |
