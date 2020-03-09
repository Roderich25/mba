#!/usr/bin/env python3
import face_recognition
import os
import cv2

KNOWN_FACES_DIR = 'known_faces'
UNKNOWN_FACES_DIR = 'unknown_faces'
TOLERANCE = 0.6
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "cnn"  # hog

print("loading known faces ...")

known_faces = []
