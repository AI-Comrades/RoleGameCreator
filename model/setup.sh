#!/bin/bash

model_name="llama2"
custom_model_name="role-game-creator-llama2"

ollama pull $model_name

ollama create $custom_model_name -f ./Modelfile