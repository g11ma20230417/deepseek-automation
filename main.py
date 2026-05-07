#!/usr/bin/env python3
"""DeepSeek 自动化系统 - 主程序"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / 'scripts'))

from scripts.deepseek_controller import DeepSeekController
from scripts.code_generator import CodeGenerator
from scripts.cross_platform_deployer import CrossPlatformDeployer


class DeepSeekAutomationSystem:
    def __init__(self):
        self.controller = DeepSeekController()
        self.generator = CodeGenerator()
        self.deployer = CrossPlatformDeployer()

    async def run_full_workflow(self, task: str, save_package: bool = True) -> dict:
        result = {
            'success': False,
            'task': task,
            'response': None,
            'package_path': None,
            'download_url': None,
            'error': None
        }

        try:
            print("\n" + "="*60)
            print("🚀 DeepSeek 自动化系统")
            print("="*60)
            print(f"\n📋 任务: {task}")

            print("\n步骤 1/5: 初始化...")
            if not await self.controller.initialize():
                raise Exception("控制器初始化失败")

            print("\n步骤 2/5: 打开 DeepSeek...")
            if not await self.controller.navigate_to_deepseek():
                raise Exception("无法打开 DeepSeek")

            print("\n步骤 3/5: 发送问题到 DeepSeek 专家模式...")
            response = await self.controller.ask(
                task, use_expert=True, use_think=True, use_search=True
            )

            if not response:
                raise Exception("未获取到响应")

            result['response'] = response

            if save_package:
                print("\n步骤 4/5: 生成跨平台代码包...")
                success, package_path = self.generator.create_package(task, response)

                if success:
                    result['package_path'] = package_path
                    print(f"  ✅ 代码包已生成")

                    print("\n步骤 5/5: 启动下载服务器...")
                    deploy_result = self.deployer.deploy(package_path, method='local')

                    if deploy_result['success']:
                        result['download_url'] = deploy_result['data'].get('url')

            print("\n✅ 工作流完成!")
            result['success'] = True
            await self.controller.close()

        except Exception as e:
            result['error'] = str(e)

        return result


async def main():
    system = DeepSeekAutomationSystem()
    if len(sys.argv) > 1:
        task = ' '.join(sys.argv[1:])
        result = await system.run_full_workflow(task)
    else:
        print("请输入任务")


if __name__ == "__main__":
    asyncio.run(main())
