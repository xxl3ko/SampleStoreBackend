def get_path_upload_sample(instance, file):
    return f'{instance.label.name}/{instance.pack.name}/samples/{file}'


def get_path_upload_cover(instance, file):
    return f'{instance.label}/{instance.name}/info/{file}'


"""def get_path_upload_cover(instance, file):
    return f'{instance.label}/{instance.name}/info/{file}'
"""