# Least recently used cache

The **Least recently used (LRU)** cache is a cache algorithm that organizes element in order of use.

### Table of content

- [What is LRU cache?](#what-is-lru-cache)
- [Operations on LRU cache](#operations-on-lru-cache)

### What is LRU cache?

Cache repalce algorithms are effeciently designed to replace the cache when the space is full. The **Least recently used (LRU)** is one of  those algorithms. When the cache memory is full, LRU picks the data that is least recently used and **removes** it in order to make space for the new data i.e. if some data is fetched or updated recently then the priority of that data would be changed and assigned to the **highest priority**, and the priority of the data **decreases** if it remains unused operations after operations.

### Operations on LRU cache

- **LRUCache (Capacity c)**: Initialize LRU cache with positive size capacity **c**.
- **get(key)**: Returns the value of key '**k**' if it is present in the cache otherwise it returns -1.
- **put(key, value)**: Update the value of the key if that key exists, Otherwise, add a **key-value** pair to the cache. If the number of keys exceeds the capacity of the LRU cache them dismess the least recently used key.