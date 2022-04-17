import os
import json
import numpy as np
from typing import Tuple, List
from lanyocr.text_recognizer.paddleocr_base import PaddleOcrBase
from lanyocr.utils import download_model


class PaddleOcrChServer(PaddleOcrBase):
    def __init__(self, use_gpu: bool = True) -> None:
        print("Recognizer: PaddleOcrChServer")

        model_h = 32
        model_w = 320

        cur_dir = os.path.dirname(os.path.realpath(__file__))

        model_ignored_tokens = [0]
        accepted_characters = json.load(
            open(os.path.join(cur_dir, "dicts/paddleocr_en_dict.json"))
        )
        # accepted_characters = []
        model_characters = json.load(
            open(os.path.join(cur_dir, "dicts/ppocr_keys_v1_mod.json"))
        )
        # model_path = os.path.join(
        #     cur_dir, "../models/lanyocr-paddleocr-db-recognizer.onnx"
        # )
        model_path = download_model("lanyocr-paddleocr-db-recognizer.onnx")

        assert os.path.exists(model_path)

        super().__init__(
            use_gpu,
            model_ignored_tokens,
            model_characters,
            accepted_characters,
            model_path,
            model_w,
            model_h,
        )