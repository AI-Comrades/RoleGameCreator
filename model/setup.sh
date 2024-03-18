#!/bin/bash

model_name="zephyr"
custom_model_name="role-game-creator-zephyr"

ollama pull $model_name

ollama create $custom_model_name -f ./Modelfile