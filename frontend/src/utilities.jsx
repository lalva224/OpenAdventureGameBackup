import axios from 'axios'

export const api = axios.create({
baseURL :'http://ec2-18-212-35-86.compute-1.amazonaws.com:8000/api/v1/adventuregame/',
})