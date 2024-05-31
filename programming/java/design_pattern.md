---
title: Design Pattern
---

## Design Pattern


## Dependency Injection
- https://martinfowler.com/articles/injection.html#UsingAServiceLocator


```java

class MovieLisner {
  public MovieLister() {
    finder = new ColonDelimitedMovieFinder("movies1.txt");
  }
  public Movie[] moviesDirectedBy(String arg) {
      List allMovies = this.finder.findAll();
      for (Iterator it = allMovies.iterator(); it.hasNext();) {
          Movie movie = (Movie) it.next();
          if (!movie.getDirector().equals(arg)) it.remove();
      }
      return (Movie[]) allMovies.toArray(new Movie[allMovies.size()]);
  }
}

interface MovieFinder {
  List findAll();
}
```

Constructor Injection with PicoContainer

```java
class MovieLister{
  public MovieLister(MovieFinder finder) {
      this.finder = finder;
  }
}

```

Setter Injection with Spring


```java
class MovieLister {
  private MovieFinder finder;
  public void setFinder(MovieFinder finder) {
    this.finder = finder;
  }
}

class ColonMovieFinder {
  public void setFilename(String filename) {
      this.filename = filename;
  }
}
/*
<beans>
    <bean id="MovieLister" class="spring.MovieLister">
        <property name="finder">
            <ref local="MovieFinder"/>
        </property>
    </bean>
    <bean id="MovieFinder" class="spring.ColonMovieFinder">
        <property name="filename">
            <value>movies1.txt</value>
        </property>
    </bean>
</beans>
*/
public void testWithSpring() throws Exception {
    ApplicationContext ctx = new FileSystemXmlApplicationContext("spring.xml");
    MovieLister lister = (MovieLister) ctx.getBean("MovieLister");
    Movie[] movies = lister.moviesDirectedBy("Sergio Leone");
    assertEquals("Once Upon a Time in the West", movies[0].getTitle());
}
```

Interface Injection

```java
interface InjectFinder {
    void injectFinder(MovieFinder finder);
}
class MovieLister implements InjectFinder {
  public void injectFinder(MovieFinder finder) {
      this.finder = finder;
  }
}
interface InjectFinderFilename {
    void injectFilename (String filename);
}
class ColonMovieFinder implements MovieFinder, InjectFinderFilename {
  public void injectFilename(String filename) {
      this.filename = filename;
  }
}

class Tester {
  private Container container;
  private void configureContainer() {
     container = new Container();
     registerComponents();
     registerInjectors();
     container.start();
  }
  private void registerComponents() {
    container.registerComponent("MovieLister", MovieLister.class);
    container.registerComponent("MovieFinder", ColonMovieFinder.class);
  }
  private void registerInjectors() {
    container.registerInjector(InjectFinder.class, container.lookup("MovieFinder"));
    container.registerInjector(InjectFinderFilename.class, new FinderFilenameInjector());
  }
  public void testIface() {
    configureContainer();
    MovieLister lister = (MovieLister)container.lookup("MovieLister");
    Movie[] movies = lister.moviesDirectedBy("Sergio Leone");
    assertEquals("Once Upon a Time in the West", movies[0].getTitle());
  }
  public static class FinderFilenameInjector implements Injector {
    public void inject(Object target) {
      ((InjectFinderFilename)target).injectFilename("movies1.txt");
    }
  }
}
```


## Service Locator
- https://martinfowler.com/articles/injection.html#UsingAServiceLocator


```java
class MovieLister{
  MovieFinder finder = ServiceLocator.movieFinder();
}
class ServiceLocator{
  private static ServiceLocator soleInstance;
  private MovieFinder movieFinder;
  public ServiceLocator(MovieFinder movieFinder) {
      this.movieFinder = movieFinder;
  }
  public static MovieFinder movieFinder() {
      return soleInstance.movieFinder;
  }
  public static void load(ServiceLocator arg) {
      soleInstance = arg;
  }
}
class Tester{
  private void configure() {
      ServiceLocator.load(new ServiceLocator(new ColonMovieFinder("movies1.txt")));
  }
  public void testSimple() {
      configure();
      MovieLister lister = new MovieLister();
      Movie[] movies = lister.moviesDirectedBy("Sergio Leone");
      assertEquals("Once Upon a Time in the West", movies[0].getTitle());
  }
}
```

## Reference
