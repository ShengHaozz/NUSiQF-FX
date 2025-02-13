import pandas as pd
import numpy as np
from Data_Processing.ir_processing import get_ir_df
from Alpha_Gen.uip_alpha_gen import uip_alpha_gen
from Asset_Alloc.wq_allocator import wq_allocator
ir_df = get_ir_df()
ir_alpha_df = uip_alpha_gen(ir_df) - 1
ir_alloc = wq_allocator(ir_alpha_df)
print(ir_alloc.head())