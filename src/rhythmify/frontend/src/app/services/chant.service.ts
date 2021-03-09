import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Chant } from '../models/chant.model';

const baseUrl = 'http://localhost:8000/api/melodies';

@Injectable({
  providedIn: 'root'
})
export class ChantService {

  constructor(private http: HttpClient) { }

  getAll(): Observable<Chant[]> {
    return this.http.get<Chant[]>(baseUrl);
  }

  get(id: any): Observable<Chant> {
    return this.http.get(`${baseUrl}/${id}`);
  }

  create(data: any): Observable<any> {
    return this.http.post(baseUrl, data);
  }

  update(id: any, data: any): Observable<any> {
    return this.http.put(`${baseUrl}/${id}`, data);
  }

  delete(id: any): Observable<any> {
    return this.http.delete(`${baseUrl}/${id}`);
  }

  deleteAll(): Observable<any> {
    return this.http.delete(baseUrl);
  }

  findByTitle(title: any): Observable<Chant[]> {
    return this.http.get<Chant[]>(`${baseUrl}?title=${title}`);
  }
}
