import config
from src.utils import boost_stat, modify_item, quick_save_load, run_custom_script

class Trainer:
    def __init__(self):
        self.stat_boost = config.STAT_BOOST
        self.item_modification = config.ITEM_MODIFICATION
        self.quick_save = config.QUICK_SAVE
        self.script_path = config.SCRIPT_PATH

    def run(self):
        boost_stat(self.stat_boost)
        if self.item_modification:
            modify_item()
        if self.quick_save:
            quick_save_load()
        if self.script_path:
            run_custom_script(self.script_path)

if __name__ == "__main__":
    trainer = Trainer()
    trainer.run()