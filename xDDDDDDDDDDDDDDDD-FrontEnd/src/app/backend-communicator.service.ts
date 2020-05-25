import {Injectable} from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';
import {Observable} from 'rxjs';
import {Plant} from './plant';

@Injectable({
  providedIn: 'root'
})
export class BackendCommunicatorService {
  private readonly getPlantsListURLPart = '/getPlantsList';
  private readonly addPlantURLPart = '/addPlant';
  private readonly backendURL = `http://${window.location.hostname}:5000`;

  constructor(private httpClient: HttpClient) {
  }

  getPlants(positionX: number, positionY: number): Observable<Plant[]> {
    const params = new HttpParams()
      .set('userPositionX', String(positionX))
      .set('userPositionY', String(positionY))
      .set('distance', '0');
    const endpointAddress = `${this.backendURL}${this.getPlantsListURLPart}`;
    return this.httpClient.get<Plant[]>(endpointAddress, {params: params});
  }

  addPlant(name: string, positionX: number, positionY: number): Observable<null> {
    const params = new HttpParams()
      .set('name', name)
      .set('positionX', String(positionX))
      .set('positionY', String(positionY));
    const endpointAddress = `${this.backendURL}${this.addPlantURLPart}`;
    return this.httpClient.get<null>(endpointAddress, {params: params});
  }
}
