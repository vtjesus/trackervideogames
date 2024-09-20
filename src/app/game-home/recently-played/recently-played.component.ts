import { Router } from '@angular/router';
import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common'; // *ngFor
import { GameItemInterface } from '../../gameItem.interface';
import { GameDataService } from '../../game-data.service';

@Component({
  selector: 'app-recently-played',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './recently-played.component.html',
  styleUrl: './recently-played.component.scss',
})
export class RecentlyPlayedComponent {
  // @Input() decorator allows the parent pass data through it.
  @Input() recentlyPlayed: GameItemInterface[] = [];

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
