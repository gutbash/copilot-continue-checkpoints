from ...core.main import Step
from ...core.sdk import Models, ContinueSDK
from ...libs.util.step_name_to_steps import get_step_from_name


class StepsOnStartupStep(Step):
    hide: bool = True

    async def describe(self, models: Models):
        return "Running steps on startup"

    async def run(self, sdk: ContinueSDK):
        steps_on_startup = sdk.config.steps_on_startup

        for step_name, step_params in steps_on_startup.items():
            step = get_step_from_name(step_name, step_params)
            await sdk.run_step(step)
