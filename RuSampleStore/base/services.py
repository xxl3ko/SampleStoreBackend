def get_path_upload_sample(instance, file):
    return f'{instance.label}/{instance.pack}/{file}'


def get_path_upload_cover(instance, file):
    return f'{instance.label}/{instance.name}/info/{file}'
