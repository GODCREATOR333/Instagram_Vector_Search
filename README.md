# Instagram_Vector_Search

## Project Overview

Instagram_Vector_Search is a personal project developed to solve the challenge of searching and managing saved posts on Instagram. By creating an application that scrapes and stores saved posts from Instagram into MongoDB, I’ve designed a solution to enhance how Instagram users can search and access their saved content. The project utilizes **SuperDuperDB** for efficient data management and integrates **OpenAI’s CLIP model** to generate multimodal embeddings for both images and videos. This enables powerful vector search capabilities, allowing users to search for saved posts using natural language or visual content.

## Key Features

- **Saved Post Scraping**: Scrapes saved posts from Instagram and stores them in a MongoDB database.
- **MongoDB & SuperDuperDB Integration**: Uses **SuperDuperDB** to efficiently manage and organize saved post data, ensuring scalability and speed.
- **Multimodal Embeddings**: Converts saved posts into multimodal embeddings using **OpenAI’s CLIP model**, enabling both image and text-based search.
- **Vector Search**: Implements **vector search** functionality that allows searching across both text and visual content, making it easy to find specific posts based on descriptions or visual similarity.
- **Instagram Saved Post Management**: Provides a backend system for saving and indexing Instagram posts in a more accessible and organized manner.

## Technologies Used

- **Instagram API**: Used to scrape saved posts from Instagram and retrieve necessary data.
- **MongoDB**: Employed for storing saved posts, allowing for fast querying and scalability.
- **SuperDuperDB**: Integrated with MongoDB to improve data management, offering enhanced indexing and efficient storage.
- **OpenAI CLIP Model**: Utilized **CLIP** to generate multimodal embeddings for images and text, enabling advanced search functionality.
- **Vector Search**: Implemented **vector search** techniques to allow searching across multimodal data (text and images).

## How It Works

1. **Scraping Instagram Saved Posts**: The application scrapes saved posts from an Instagram account using the Instagram API.
2. **Storing Data in MongoDB**: Saved posts, along with relevant metadata (e.g., image/video URLs, captions), are stored in MongoDB.
3. **Multimodal Embeddings**: The data is processed using the CLIP model to create multimodal embeddings (both visual and textual) for each post.
4. **Vector Indices**: These embeddings are then indexed using vector search techniques, allowing efficient searching across multimodal data.
5. **Search Interface**: Users can query the database with either textual descriptions or images, and the system retrieves the most relevant saved posts based on similarity.
