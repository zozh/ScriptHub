/*
 * @Author: zouzhao
 * @Date: 2023-09-26 11:16:41
 * @LastEditors: zouzhao
 * @LastEditTime: 2023-09-26 11:16:57
 * @Description: 
 * 
 * Copyright (c) 2023 by zouzhao, All Rights Reserved. 
 */
const { app, BrowserWindow } = require("electron")
const path = require("path")

function createWindow () {
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
  })

  mainWindow.loadFile(path.join(__dirname, "renderer","dist\\index.html"))
}

app.whenReady().then(() => {
  createWindow()

  app.on("activate", function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})
