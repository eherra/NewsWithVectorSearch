# News Search with vectors
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)


>  Introduction to Data Science mini-project


## How to run

Fill <code>.envs</code> in backend folder. See the [.env.example](https://github.com/eherra/NewsWithVectorSearch/blob/main/backend/.env.example)

Go to root folder and run:

```
docker build -t news-vector-search .
```

and then:

```
docker run -dp 5000:5000 -e PORT=5000 news-vector-search
```

The app is running on: http://localhost:5000/