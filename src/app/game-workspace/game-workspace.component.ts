import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
// import { Router } from '@angular/router';
import { RouterOutlet } from '@angular/router';
import { GameItemInterface } from '../gameItem.interface';
import { GameDataService } from '../game-data.service';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { faBars, faArrowLeft } from '@fortawesome/free-solid-svg-icons';
import { ElementRef, ViewChild } from '@angular/core';
import { NgOptimizedImage } from '@angular/common';

@Component({
  selector: 'app-game-workspace',
  standalone: true,
  imports: [CommonModule, RouterOutlet, FontAwesomeModule, NgOptimizedImage],
  templateUrl: './game-workspace.component.html',
  styleUrl: './game-workspace.component.scss',
})
export class GameWorkspaceComponent implements OnInit {
  faBars = faBars;
  faBack = faArrowLeft;

  games: GameItemInterface[] = [];
  game: GameItemInterface | undefined;

  @ViewChild('sidebarContainer') sidebarContainer!: ElementRef;

  constructor(
    // private router: Router,
    private gameDataService: GameDataService,
  ) {}

  ngOnInit(): void {
    if (this.gameDataService.isDataLoaded()) {
      this.games = this.gameDataService.getGamesData();
    } else {
      fetch('public/games.json')
        .then((response) => response.json())
        .then((data: GameItemInterface[]) => {
          this.games = data;
          this.gameDataService.setGamesData(data); // Store data in service
        })
        .catch((error) => console.error('Error loading GameData:', error));
    }

    this.scrollToSelectedGame()

    // Subscribe to changes
    this.gameDataService.selectedGameChanged.subscribe({
      next: (game: GameItemInterface | undefined) => {
        this.game = game;
      },
      error: (err) => console.error('Error loading game:', err),
    });
  }

  // Scroll to selected game in Sidebar
  scrollToSelectedGame(): void {
    setTimeout(() => {
      const selectedElement = document.getElementById('selected-game');
      console.log(
        'log: Finding scrollbar selected element: ' +
          selectedElement?.innerText,
      );
      if (selectedElement) {
        selectedElement.scrollIntoView({
          behavior: 'smooth', // smooth | instant
          block: 'center', // nearest | end | start | center
        });
      }
    }, 100); // Wait for DOM
  }

  viewDetails(game: GameItemInterface): void {
    this.gameDataService.setSelectedGame(game);
    console.log('log: Sending data to /game-details: ' + game);
    // this.router.navigate(['workspace/game-details']);
  }
}
