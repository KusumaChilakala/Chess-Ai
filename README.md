Chess AI 🎯♟️
A fully functional Chess Game with AI, built using Python, Pygame, and Stockfish. Play against a strong AI opponent with an interactive GUI, smooth animations, and enhanced move visualization with black dotted lines.

🚀 Features
✅ Interactive Chessboard – Click to move pieces using a graphical interface
✅ AI Opponent (Stockfish) – Play against a powerful chess engine
✅ Valid Move Highlighting – Displays all possible moves with black dotted lines
✅ Checkmate & Stalemate Detection – Game ends when no valid moves remain
✅ Piece Capture & Special Moves – Supports castling, en passant, and pawn promotion
✅ Smooth Animations – Pieces move seamlessly on the board

🛠️ Tech Stack
Python – Core game logic
Pygame – GUI rendering for the chessboard & pieces
Python-Chess – Chess logic, move validation, and legal moves
Stockfish – AI engine for strong computer moves

🎮 How to Play
Click on a piece to select it.
Black dotted lines will indicate possible move directions.
Click on a valid square to move the piece.
The AI will automatically respond after your move.
The game continues until checkmate, stalemate, or draw.

chess-ai-game/
│── images/                # Chess piece images (wp.png, bp.png, etc.)
│── chess_game.py          # Main Pygame GUI for playing chess
│── ai.py                  # AI logic (if separate from main file)
│── stockfish.exe          # Chess engine (Download separately)
│── README.md              # Project documentation
└── requirements.txt       # Dependencies list
🔥 Future Enhancements
🚀 Multiplayer Mode – Play against another human online
🎨 Better UI/Animations – Enhanced visuals & piece movement effects
📱 Web Version – Implement using React & Flask
🧠 Custom AI – Replace Stockfish with Minimax-based AI
