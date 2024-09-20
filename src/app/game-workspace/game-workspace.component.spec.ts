import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GameWorkspaceComponent } from './game-workspace.component';

describe('GameWorkspaceComponent', () => {
  let component: GameWorkspaceComponent;
  let fixture: ComponentFixture<GameWorkspaceComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GameWorkspaceComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GameWorkspaceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
