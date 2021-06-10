# Root Me

- Download the [`PDF`](https://github.com/a3X3k/RoadMap/blob/main/Set%203/PDF/1.pdf) given.
- Analyse using `Peepdf`.
- [`Reference 1`](https://eternal-todo.com/tools/peepdf-pdf-analysis-tool) [`Reference 2`](https://singhgurjot.wordpress.com/2015/04/15/how-to-use-peepdf-suspecious-pdf-in-kali-linux/)

![](https://github.com/a3X3k/RoadMap/blob/main/Set%203/PDF/2.png?raw=true)

- We shall see that there are `2 Streams`.
- We shall see there is an `embedded file` in the `PDF`.
- So now we need to extract the `embedded file` using the `stream` command.
- We shall see that there is an `PNG` Image in `stream 8`.
- Now lets redirect the output to the `PNG` file.

```
PPDF> stream 8 > 1.PNG
```

- Now we shall get a [`PNG`](https://github.com/a3X3k/RoadMap/blob/main/Set%203/PDF/1.png?raw=true) Image.
