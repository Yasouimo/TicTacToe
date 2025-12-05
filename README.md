# Tic-Tac-Toe AI with Python & Pygame 

This is a Python implementation of Tic-Tac-Toe with an AI opponent using the Minimax algorithm. The game features a graphical user interface (GUI) built with Pygame, allowing a human player to compete against an intelligent computer opponent.

## Introduction

Tic-Tac-Toe is a classic two-player game where each player takes turns placing "X" or "O" on a 3x3 grid. The goal is to get three marks in a row, column, or diagonal before the opponent. This project implements:
- A Minimax AI that makes optimal moves.
- A graphical game board using Pygame.
- Interactive player selection and move handling.

## Game States

### Initial State (Before Game Starts)
At the beginning, the player can choose to play as **X** or **O**.

![Image](https://github.com/user-attachments/assets/8c27dd48-cac0-4a7c-ba84-cab18c0a8e19)

### Final State (Win, Draw, or Lose)
After playing, the game will display the result:
- **Win:** If the player gets three in a row.
- **Lose:** If the AI gets three in a row.
- **Tie:** If the board is full with no winner.

![Image](https://github.com/user-attachments/assets/7bdc259e-8b7e-4441-b75a-932c8963351d)

## How to Run the Project

### Prerequisites
Ensure you have Python installed. You also need `pygame`.

### Install Dependencies
Run the following command to install required packages:

```bash
pip install -r requirements.txt
