import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
// import { Router } from '@angular/router';
import { GameItemInterface } from '../../gameItem.interface';
import { GameDataService } from '../../game-data.service';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import {
  faClock,
  faStar,
  faCalendar,
  faGlobe,
  faUser,
  faGears,
  faMasksTheater,
  faGun,
  faEye,
  faGamepad,
} from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-game-details',
  standalone: true,
  imports: [CommonModule, FontAwesomeModule],
  templateUrl: './game-details.component.html',
  styleUrl: './game-details.component.scss',
})
export class GameDetailsComponent implements OnInit {
  faClock = faClock;
  faStar = faStar;
  faCalendar = faCalendar;
  faGlobe = faGlobe;
  faUser = faUser;
  faGears = faGears;
  faMasksTheater = faMasksTheater;
  faGun = faGun;
  faEye = faEye;
  faGamepad = faGamepad;

  game: GameItemInterface | undefined;
  playtimeHours: number | undefined;
  playtimeMinutes: number | undefined;

  constructor(
    // private router: Router,
    private gameDataService: GameDataService,
  ) {}

  ngOnInit(): void {
    this.game = this.gameDataService.getSelectedGame();
    console.log('log: Recieved on /game-details: ' + this.game);

    // Subscribe to changes
    this.gameDataService.selectedGameChanged.subscribe({
      next: (game: GameItemInterface | undefined) => {
        this.game = game;
        if (this.game && this.game.playtime) {
          console.log('log: Calculating time: ' + this.game.playtime);
          this.calculatePlaytime(this.game.playtime);
        }
      },
      error: (err) => console.error('Error loading game:', err),
    });

    // DEFAULT DATA
    if (!this.game) {
      // this.router.navigate(['/']);
      this.game = {
        id: 69,
        name: 'Game Completion Tracker',
        year: 2024,
        developer: 'Mid Hunter',
        description:
          'This is an Angular-based single-page application (SPA) designed to help me share my game completions and stay organized with my gaming activities. The platform offers a visually engaging and user-friendly interface, where others can explore details about various games, track my progress, and navigate seamlessly between game details.',
        website: 'https://midhunterx.github.io/',
        game_engines: ['Angular 14'],
        player_modes: ['Single player'],
        platforms: ['GNU / Linux', 'Microsoft Windows', 'MacOS'],
        pov: ['Website', 'SPA'],
        genres: ['Game Tracking', 'Completion List', 'IGDB'],
        themes: ['Gaming'],
        keywords: [
          'It',
          'is',
          'my',
          'first time',
          'developing',
          'in',
          'Angular',
        ],
        img: '+',
        playtime: 22140,
        rating: 69,
      };
      this.gameDataService.setSelectedGame(this.game);
    }

    if (this.game && this.game.playtime) {
      console.log('log: Calculating time: ' + this.game.playtime);
      this.calculatePlaytime(this.game.playtime);
    }
  }

  calculatePlaytime(playtimeInSeconds: number): void {
    this.playtimeHours = Math.floor(playtimeInSeconds / 3600);
    this.playtimeMinutes = Math.floor((playtimeInSeconds % 3600) / 60);
  }
}
