import { Component, OnInit } from '@angular/core';
import { MatDialog, MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.scss']
})
export class BoardComponent implements OnInit {

  board!: string[];

  xIsNext!: boolean;

  winner!: string | null;

  allMov!: number[];

  constructor(public dialog: MatDialog) {
  }

  ngOnInit(): void {
    this.startNewGame();
  }

  get player(): string {
    return this.xIsNext ? 'X' : 'O';
  }

  startNewGame(): void {
    this.board = new Array<string>(9).fill(null);
    this.xIsNext = true;
    this.winner = null;
    this.allMov = new Array<number>;
  }

  makeMove(index: number): void {
    if (!this.board[index]) {
      this.board[index] = this.player;
      this.xIsNext = !this.xIsNext;
      this.winner = this.checkWinner();
      this.allMov.push(index);
      if (this.winner != null)
        this.displayWinnerDialog();
      else if (this.allMov.length == 9) 
        this.displayEqualityDialog();
    }
  }

  undo(): void {
    if (this.allMov.length > 0) {
      if (this.winner != null)
        this.winner = null;
      let index = this.allMov.pop();
      this.board[index] = null;
      this.xIsNext = !this.xIsNext;
    }
    else
      window.alert("no movement left");
  }

  checkWinner(): string {
    const lines = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6]
    ];

    for (let i = 0; i < lines.length; ++i) {
      const [a, b, c] = lines[i];
      if (this.board[a] != null && this.board[a] == this.board[b] && this.board[b] == this.board[c])
        return this.board[a];
    }
    return null;
  }

  displayWinnerDialog(): void {
    const dialogRef = this.dialog.open(WinnerDialog);
    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }

  displayEqualityDialog(): void {
    const dialogRef = this.dialog.open(EqualityDialog);
    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }
    

}

@Component({
  selector: 'winner-dialog',
  templateUrl: './winner-dialog.html',
})
export class WinnerDialog {
  // @Inject(Component) winner: string, 
  constructor(public dialogRef: MatDialogRef<WinnerDialog>) {
  }
}

@Component({
  selector: 'equality-dialog',
  templateUrl: './equality-dialog.html',
})
export class EqualityDialog {
  constructor(public dialogRef: MatDialogRef<EqualityDialog>) {
  }
}