# Tic-Tac-Toe (X-O) Robotic Manipulator

## Description  
This project combines image processing, artificial intelligence, and robotics to enable a Poppy humanoid robotic arm to play Tic-Tac-Toe against a human opponent. The system uses a Logitech HD Webcam C270 for real-time image acquisition, processes the game state with Python and OpenCV, and employs AI to determine optimal moves. The robotic arm, equipped with an electromagnetic end effector, places X markers on the board based on the AI's decisions. The hardware setup includes 3D-printed parts, servo motors, and an Arduino Uno for control. The project integrates computer vision, trajectory simulation, and game logic to create an interactive and educational robotic demonstrator.

## Key Aspects  
- **Hardware**: Poppy robotic arm with 5V electromagnetic end effector, 3D-printed components, and Arduino Uno for servo control.  
- **Image Processing**: OpenCV-based techniques (grayscale conversion, thresholding, Hough transforms) to detect board state and player moves.  
- **AI Integration**: Minimax algorithm or lookup tables for optimal move prediction.  
- **Simulation**: Trajectory planning and testing using Simscape Multibody and SolidWorks.  
- **Educational Focus**: Demonstrates robotics, AI, and computer vision principles for student learning.  

## Components  
- **Robotic Arm**: Custom 3D-printed manipulator with 4 servo motors.  
- **Sensors**: Logitech C270 camera for board monitoring.  
- **Control**: Arduino Uno interfaced with Python for real-time decision execution.  
- **Game Board**: 60cm × 60cm grid with metallic X markers for electromagnetic pickup.  

## Project Workflow  
1. **Hardware Assembly**: Fabricate and connect robotic arm, camera, and power supply.  
2. **Image Processing**: Implement board detection, move recognition, and state updates.  
3. **AI Decision-Making**: Integrate game logic (e.g., Minimax) to determine robotic moves.  
4. **Motion Control**: Simulate and execute arm trajectories to place markers.  
5. **Testing**: Validate system under varying lighting and gameplay scenarios.  

## References  
1. Thormann et al., *Playing Tic-Tac-Toe with a Lightweight Robot* (Springer, 2022).  
2. Jiao et al., *Intelligent Single-Pixel Imaging for Tic-Tac-Toe* (arXiv, 2022).  
3. Karmanova et al., *SwarmPlay: Nano-UAVs Driven by Reinforcement Learning* (IEEE RO-MAN, 2021).  

*Developed by Ibrahim Elsahhar, Hana Ahmed, Marwan Sallam, Farida Moubarak, and Amr Abd El-Latif at the German University in Cairo (GUC).*  
