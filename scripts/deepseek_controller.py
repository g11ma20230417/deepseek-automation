#!/usr/bin/env python3
"""DeepSeek 浏览器控制器"""

import asyncio
from playwright.async_api import async_playwright


class DeepSeekController:
    def __init__(self):
        self.browser = None
        self.context = None
        self.page = None

    async def initialize(self):
        print("🌐 正在启动浏览器...")
        try:
            playwright = await async_playwright().start()
            self.browser = await playwright.chromium.launch(headless=False)
            self.context = await self.browser.new_context()
            self.page = await self.context.new_page()
            return True
        except Exception as e:
            print(f"❌ 浏览器启动失败: {e}")
            return False

    async def navigate_to_deepseek(self):
        try:
            print("🔗 正在打开 DeepSeek...")
            await self.page.goto("https://chat.deepseek.com", wait_until="networkidle")
            await asyncio.sleep(3)
            return True
        except Exception as e:
            print(f"❌ 导航失败: {e}")
            return False

    async def check_login(self):
        try:
            login_btn = await self.page.query_selector('button:has-text("登录")')
            if login_btn:
                print("⚠️  请登录 DeepSeek（60秒）")
                await asyncio.sleep(60)
                return await self.check_login()
            return True
        except:
            return True

    async def activate_modes(self, expert=True, think=True, search=True):
        print("🔧 激活功能模式...")
        try:
            await self.page.click('[class*="model-selector"]', timeout=5000)
            await asyncio.sleep(1)
            
            if expert:
                await self.page.click('text=DeepSeek-R1', timeout=5000)
                print("  ✅ 专家模式")
            
            if think:
                await self.page.click('text=深度思考', timeout=5000)
                print("  ✅ 深度思考")
            
            if search:
                await self.page.click('text=联网搜索', timeout=5000)
                print("  ✅ 联网搜索")
                
        except Exception as e:
            print(f"  ⚠️  部分功能可能已启用: {e}")

    async def ask(self, question, use_expert=True, use_think=True, use_search=True):
        await self.check_login()
        await self.activate_modes(use_expert, use_think, use_search)
        
        print(f"📤 发送: {question[:50]}...")
        textarea = await self.page.query_selector('textarea')
        if not textarea:
            print("❌ 未找到输入框")
            return None
        
        await textarea.fill(question)
        await self.page.keyboard.press('Enter')
        
        print("⏳ 等待响应...")
        await asyncio.sleep(30)
        
        messages = await self.page.query_selector_all('[class*="message-content"]')
        if messages:
            return await messages[-1].inner_text()
        return None

    async def close(self):
        if self.browser:
            await self.browser.close()
            print("👋 浏览器已关闭")
