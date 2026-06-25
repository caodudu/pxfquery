import os
import anndata as ad
import scanpy as sc
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import re
from typing import Union
from openai import OpenAI
import json

from .prompt.check_link import check_link


class pxfquery():
    def __init__(self,):
        pass 

    def load_pxf(self, path: Union[str,None]=None):
        '''
        1. 允许本地指定路径寻找，
        2. 如果发现路径是空的，就去联网下载(github?还是那个什么网站)到这个路径
        3.
        '''
        pass 


    def load_llm(
        self, 
        api_key: Union[str,None]=None, 
        url: Union[str,None]=None,
        model: Union[str,None]=None,):
        '''
        1. 加载api。允许本地或者外地。
        2. 构建查询
        '''
        #api_key = os.getenv("SILICONFLOW_API_KEY")

        # 创建 client 并指定 base_url
        #client = OpenAI(
        #    api_key=api_key,
        #    base_url="https://api.siliconflow.cn/"  # 硅基流动 API 的根路径
        #)
        # 1. 加载llm
        self.client = OpenAI(
            api_key=api_key,
            base_url=url  
        )
        self.model = model
        # 2. 测试联通
        self.load_llm = check_link(self.client,self.model)

    def load_anno(self, path: Union[str,None]=None):
        '''
        服务于几个清洗命令
        '''
        pass

    def pert2func(self,):
        '''

        '''
        pass

    def func2pert(self,):
        '''

        '''
        pass


    def _parse_user_query(self,):
        '''
        1. 识别用户任务类型，是正向查询还是反向查询
        2. 识别生物背景描述部分，
        3. 提取功能描述部分
        4. 提取扰动描述部分
        '''
        pass 


    def _bio_match(self,):
        '''
        1. 细胞背景的清洗锁定

        已有细胞系那就直接锁定
        没有的话用相近
        '''
        pass 


    def _pert_match(self,):
        '''
        2. 扰动的清洗锁定
        '''
        pass 


    def _func_match(self,):
        '''
        功能词条的清洗锁定
        '''
        pass

    def _summary_p2f(self,):
        '''
        '''
        pass 
    
    def _summary_f2p(self,):
        '''
        '''
        pass


    def plot_pert2func(self,):
        '''
        '''
        pass 

    def plot_func2pert(self,):
        '''
        '''
        pass 