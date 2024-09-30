grid_args = dict(
    canonical_num_levels=16,
    canonical_level_dim=2,
    canonical_base_resolution=16,
    canonical_desired_resolution=2048,
    canonical_log2_hashmap_size=19,

    deform_num_levels=32,
    deform_level_dim=2,
    deform_base_resolution=16,
    deform_desired_resolution=[512, 512, 128],
    deform_log2_hashmap_size=19,

    bound=30.0,
)

network_args = dict(
    depth=0,
    width=256,
    directional=True,
)

load2gpu_on_the_fly = True

grid_lr_scale = 50.0
network_lr_scale = 1.0

lambda_spatial_tv = 0.5
spatial_downsample_ratio = 1.0
spatial_perturb_range = 5e-3

lambda_temporal_tv = 0.5
temporal_downsample_ratio = 1.0
temporal_perturb_range = [5e-3, 5e-3, 5e-3, 0.0]

disable_ws_prune = True
# iterations = 40_000

iterations = 20_000
densification_interval = 400
opacity_reset_interval = 6000
reg_after_densify = True
# end