document.addEventListener('DOMContentLoaded', () => {
    const cells = document.querySelectorAll('.cell');
    const statusMessage = document.getElementById('status-message');
    const board = Array.from({ length: 9 }, () => ' ');
    let currentPlayer = 'O';

    function checkWinner(board) {
        const winConditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  // rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  // columns
            [0, 4, 8], [2, 4, 6]              // diagonals
        ];
        for (const [a, b, c] of winConditions) {
            if (board[a] !== ' ' && board[a] === board[b] && board[a] === board[c]) {
                return board[a];
            }
        }
        return board.includes(' ') ? null : 'tie';
    }

    function renderBoard() {
        cells.forEach((cell, index) => {
            cell.textContent = board[index];
        });
    }

    function handleClick(e) {
        const index = e.target.dataset.index;
        if (board[index] === ' ' && currentPlayer === 'O') {
            board[index] = 'O';
            currentPlayer = 'X';
            renderBoard();
            const winner = checkWinner(board);
            if (winner) {
                updateStatus(winner);
            } else {
                aiMove();
            }
        }
    }

    function aiMove() {
        const emptyCells = board.map((v, i) => v === ' ' ? i : null).filter(v => v !== null);
        const randomMove = emptyCells[Math.floor(Math.random() * emptyCells.length)];
        board[randomMove] = 'X';
        currentPlayer = 'O';
        renderBoard();
        const winner = checkWinner(board);
        if (winner) {
            updateStatus(winner);
        }
    }

    function updateStatus(winner) {
        if (winner === 'tie') {
            statusMessage.textContent = 'It\'s a tie!';
        } else {
            statusMessage.textContent = `${winner} wins!`;
        }
        cells.forEach(cell => cell.removeEventListener('click', handleClick));
    }

    cells.forEach(cell => {
        cell.addEventListener('click', handleClick);
    });
});
