import { Router } from '@angular/router';
import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common'; // *ngFor
import { GameItemInterface } from '../../gameItem.interface';
import { GameDataService } from '../../game-data.service';
import { NgOptimizedImage } from '@angular/common';

@Component({
  selector: 'app-game-cards', // HTML Tag Name
  standalone: true,
  imports: [CommonModule, NgOptimizedImage],
  templateUrl: './game-cards.component.html',
  styleUrl: './game-cards.component.scss',
})
export class GameCardsComponent {
  // @Input() decorator allows the parent pass data through it.
  @Input() remainingGames: GameItemInterface[] = [];

  // Router to pass down single Game Details down a route
  constructor(
    private router: Router,
    private gameDataService: GameDataService,
  ) {}

  viewDetails(game: GameItemInterface): void {
    this.gameDataService.setSelectedGame(game);
    console.log('log: Sending data to /game-details: ' + game);
    this.router.navigate(['workspace/game-details']);
    // this.router.navigate(['/game-details', game.id]);
  }
}
