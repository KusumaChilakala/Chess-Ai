# Chess-Ai
A fully functional chess game built using Python, Pygame, and Stockfish AI. Play against a strong AI opponent powered by Stockfish, with a simple and interactive GUI.

Features
✅ Interactive Chessboard – Click to move pieces using a graphical interface
✅ AI Opponent (Stockfish) – Play against a powerful chess engine
✅ Valid Move Highlighting – Only legal moves can be played
✅ Checkmate & Stalemate Detection – Game ends when no valid moves are available
✅ Piece Capture & Special Moves – Supports castling, en passant, and pawn promotion
✅ Smooth Animations – Pieces move smoothly on the board

Tech Stack
Python – Core logic & game handling
Pygame – GUI rendering for the chessboard & pieces
Python-Chess – Chess logic & move validation
Stockfish – AI engine for strong computer moves

Installation & Setup
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/chess-ai-game.git
cd chess-ai-game
2. Install Dependencies
Ensure you have Python installed (>=3.8). Install required libraries:

bash
Copy
Edit
pip install pygame chess
3. Download & Install Stockfish
Windows: Download Stockfish from here and place stockfish.exe in the project folder.
Linux/Mac: Install via package manager:
bash
Copy
Edit
sudo apt install stockfish  # Linux
brew install stockfish      # macOS
4. Run the Game
bash
Copy
Edit
python chess_game.py
How to Play
Click a piece to select it.
Click a valid destination square to move it.
AI will automatically respond after your move.
The game continues until checkmate, stalemate, or draw.
Project Structure
graphql
Copy
Edit
chess-ai-game/
│── images/                # Chess piece images (wp.png, bp.png, etc.)
│── chess_game.py          # Main Pygame GUI for playing chess
│── ai.py                  # AI logic (if separate from main file)
│── stockfish.exe          # Chess engine (Download separately)
│── README.md              # Project documentation
└── requirements.txt       # Dependencies list
Future Enhancements
🚀 Multiplayer Mode – Play against another human over a network
🎨 Better UI/Animations – Smooth transitions & piece highlighting
📱 Web Version – Implement using React & Flask
🧠 Custom AI – Replace Stockfish with Minimax-based AI

Contributing
Feel free to fork this repository and submit pull requests. Any contributions, bug reports, or suggestions are welcome!

License
This project is open-source and available under the MIT License.
