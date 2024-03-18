#!/bin/bash

model_name="MODEL_NAME_FROM_MODELFILE"
custom_model_name="YOUR_CUSTOM_NAME"

ollama pull $model_name

ollama create $custom_model_name -f ./Modelfile