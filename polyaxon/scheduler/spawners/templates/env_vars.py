from kubernetes import client


def get_from_experiment_config_map(name, key_name):
    config_map_key_ref = client.V1ConfigMapKeySelector(name=name, key=key_name)
    value_from = client.V1EnvVarSource(config_map_key_ref=config_map_key_ref)
    return client.V1EnvVar(name=key_name, value_from=value_from)


def get_from_secret(name, key_name):
    secret_key_ref = client.V1SecretKeySelector(name=name, key=key_name)
    value_from = client.V1EnvVarSource(secret_key_ref=secret_key_ref)
    return client.V1EnvVar(name=key_name, value_from=value_from)


def get_from_secret(key_name, key):
    secret_key_ref = client.V1SecretKeySelector(name=secret_ref_name, key=key)
    value = client.V1EnvVarSource(secret_key_ref=secret_key_ref)
    return client.V1EnvVar(name=key_name, value_from=value)


def get_env_var(name, value, reraise=True):
    if not isinstance(value, str):
        try:
            value = json.dumps(value)
        except (ValueError, TypeError) as e:
            if reraise:
                raise e

    return client.V1EnvVar(name=name, value=value)