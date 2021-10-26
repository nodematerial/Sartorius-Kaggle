_base_ = [
    '../_base_/models/cascade_mask_rcnn_r50_fpn.py',
    'base/sartorius_instance.py',
    'base/schedule_1x.py', 
    'base/default_runtime.py'
]
