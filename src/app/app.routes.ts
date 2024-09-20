import { Routes } from '@angular/router';
import { GameHomeComponent } from './game-home/game-home.component';
import { GameDetailsComponent } from './game-workspace/game-details/game-details.component';
import { GameWorkspaceComponent } from './game-workspace/game-workspace.component';

export const routes: Routes = [
  { path: '', component: GameHomeComponent },

  {
    path: 'workspace',
    component: GameWorkspaceComponent,
    children: [{ path: 'game-details', component: GameDetailsComponent }],
  },

  // { path: 'game-details/:id', component: GameDetailsComponent },
];
