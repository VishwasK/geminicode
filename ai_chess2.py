import streamlit as st
import chess
import chess.engine

# Initialize the chess engine
engine = chess.engine.SimpleEngine.popen_uci("/path/to/stockfish")

# Create a new chess game
game = chess.Board()

# Set up the streamlit app
st.title("Chess with GPT-4o-mini")
st.write("You are playing against GPT-4o-mini. Make your move:")

# Get the user's move
move = st.text_input("Move:")

# If the user has made a move, update the game state
if move:
    try:
        game.push_san(move)
    except ValueError:
        st.write("Invalid move.")

# Get the AI's move
ai_move = engine.play(game, chess.engine.Limit(time=0.1))

# Update the game state
game.push(ai_move.move)

# Display the updated game state
st.write(game.unicode())

# Check if the game is over
if game.is_game_over():
    st.write("Game over.")
    if game.is_checkmate():
        st.write("You win!")
    elif game.is_stalemate():
        st.write("Draw.")
    else:
        st.write("You lose.")

# Close the engine
engine.quit()