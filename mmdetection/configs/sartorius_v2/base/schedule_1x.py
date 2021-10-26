# optimizer
optimizer = dict(type='Adam', lr=0.005)
optimizer_config = dict(grad_clip=None)
# learning policy
lr_config = dict(
    policy='CosineAnnealing')

runner = dict(type='EpochBasedRunner', max_epochs=30)
