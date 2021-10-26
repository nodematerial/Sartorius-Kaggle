# optimizer
optimizer = dict(type='Adam', lr=0.005)
# learning policy
lr_config = dict(
    policy='CosineAnnealing')

runner = dict(type='EpochBasedRunner', max_epochs=30)
