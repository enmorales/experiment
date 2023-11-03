#!/bin/bash

#-------------------------------------------------------------------------------------------
# Profiles
#-------------------------------------------------------------------------------------------

IMAGE_PROFILE_NAME="perfiles"
IMAGE_PROFILE_VERSION="1.0"
IMAGE_PROFILE_DIR="./perfiles"

if docker inspect "$IMAGE_PROFILE_NAME:$IMAGE_PROFILE_VERSION" >/dev/null 2>&1; then
  echo "Removing existing image: $IMAGE_PROFILE_NAME:$IMAGE_PROFILE_VERSION"
  docker rmi -f "$IMAGE_PROFILE_NAME:$IMAGE_PROFILE_VERSION"
fi

echo "Building new image: $IMAGE_PROFILE_NAME:$IMAGE_PROFILE_VERSION"
docker build -t "$IMAGE_PROFILE_NAME:$IMAGE_PROFILE_VERSION" "$IMAGE_PROFILE_DIR"

#-------------------------------------------------------------------------------------------
# Machine Engine
#-------------------------------------------------------------------------------------------

IMAGE_MATCHING_ENGINE_NAME="motor-emparejamiento"
IMAGE_MATCHING_ENGINE_VERSION="1.0"
IMAGE_MATCHING_ENGINE_DIR="./motor-emparejamiento"

if docker inspect "$IMAGE_MATCHING_ENGINE_NAME:$IMAGE_MATCHING_ENGINE_VERSION" >/dev/null 2>&1; then
  echo "Removing existing image: $IMAGE_MATCHING_ENGINE_NAME:$IMAGE_MATCHING_ENGINE_VERSION"
  docker rmi -f "$IMAGE_MATCHING_ENGINE_NAME:$IMAGE_MATCHING_ENGINE_VERSION"
fi

echo "Building new image: $IMAGE_MATCHING_ENGINE_NAME:$IMAGE_MATCHING_ENGINE_VERSION"
docker build -t "$IMAGE_MATCHING_ENGINE_NAME:$IMAGE_MATCHING_ENGINE_VERSION" "$IMAGE_MATCHING_ENGINE_DIR"

#-------------------------------------------------------------------------------------------
# Validator
#-------------------------------------------------------------------------------------------

IMAGE_VALIDATOR_NAME="validador"
IMAGE_VALIDATOR_VERSION="1.0"
IMAGE_VALIDATOR_DIR="./validador"

if docker inspect "$IMAGE_VALIDATOR_NAME:$IMAGE_VALIDATOR_VERSION" >/dev/null 2>&1; then
  echo "Removing existing image: $IMAGE_VALIDATOR_NAME:$IMAGE_VALIDATOR_VERSION"
  docker rmi -f "$IMAGE_VALIDATOR_NAME:$IMAGE_VALIDATOR_VERSION"
fi

echo "Building new image: $IMAGE_VALIDATOR_NAME:$IMAGE_VALIDATOR_VERSION"
docker build -t "$IMAGE_VALIDATOR_NAME:$IMAGE_VALIDATOR_VERSION" "$IMAGE_VALIDATOR_DIR"