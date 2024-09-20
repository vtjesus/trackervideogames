import { BehaviorSubject } from 'rxjs';
import { Injectable } from '@angular/core';
import { GameItemInterface } from './gameItem.interface';

@Injectable({
  providedIn: 'root',
})
export class GameDataService {
  constructor() {}

  // FOR HOME ROUTE
  private gamesData: GameItemInterface[] = [];

  setGamesData(data: GameItemInterface[]): void {
    this.gamesData = data;
  }

  getGamesData(): GameItemInterface[] {
    return this.gamesData;
  }

  isDataLoaded(): boolean {
    return this.gamesData.length > 0;
  }

  // FOR GAME DETAILS ROUTE
  private selectedGameSubject = new BehaviorSubject<
    GameItemInterface | undefined
  >(undefined);
  selectedGameChanged = this.selectedGameSubject.asObservable();
  // private selectedGame: GameItemInterface | undefined;


  setSelectedGame(game: GameItemInterface): void {
    this.selectedGameSubject.next(game);
    // this.selectedGame = game;
  }

  getSelectedGame(): GameItemInterface | undefined {
    return this.selectedGameSubject.getValue();
    // return this.selectedGame;
  }

  // FOR DUMMY TESTING
  isDevelopment(): boolean {
    return false;
  }
}
