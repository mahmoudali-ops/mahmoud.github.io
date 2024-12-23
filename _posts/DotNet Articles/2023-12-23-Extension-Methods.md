---
title: Extension Methods
classes: wide
header:
  teaser: https://github.com/user-attachments/assets/d63efa88-81bc-4e2c-b2ec-7674b3889bbc
ribbon: MidnightBlue
categories:
  - DotNet_Articles
toc: true
---

# شرح Extension Methods

**بص يا صاحبي،** الـ Extension Methods دي حاجة جامدة جدًا في C#. هي ببساطة طريقة تخليك تضيف دوال جديدة لأي كلاس أو نوع موجود أصلاً، من غير ما تحتاج تلمس الكود الأصلي بتاعه. 

يعني إيه؟ يعني مثلاً عندك كلاس جاهز زي `string` أو `List<int>`، وعايز تضيف دالة جديدة ليه، زي دالة بتعمل حاجة مش موجودة أصلاً. بدل ما تقعد تعمل subclass أو helper functions منفصلة، بتستخدم *Extension Methods* وتخلي الدالة تبان كأنها جزء من النوع ده.

---

## طيب بنعملها إزاي؟

1. **بنكتب كلاس static:** لأن الـ Extension Methods لازم تعيش جوه كلاس static.
2. **بنضيف دالة static:** الدالة نفسها تكون static.
3. **بنحط `this` قبل أول بارامتر:** الكلمة دي هي السر، لأنها بتقول إن الدالة دي مرتبطة بالنوع اللي عايز تضيف عليه.

---

### مثال سهل: 

تخيل معايا عندك كلاس `Person` بالشكل ده:

```csharp
public class Person
{
    public string Name { get; set; }
    public DateTime BirthDate { get; set; }
}
```
وعايز تضيف طريقة تحسب عمر الشخص. بدل ما تعدل على الكلاس الأصلي، تعمل Extension Method بالشكل ده:
```csharp
public static class PersonExtensions
{
    public static int GetAge(this Person person)
    {
        DateTime today = DateTime.Today;
        int age = today.Year - person.BirthDate.Year;

        if (person.BirthDate > today.AddYears(-age))
            age--;

        return age;
    }
}

```
لما تيجي تستخدمها بقى، هتعمل كده:
```csharp
Person person = new Person { Name = "Ali", BirthDate = new DateTime(1990, 6, 15) };
int age = person.GetAge();
Console.WriteLine($"{person.Name} is {age} years old.");
```

### فهمت الفكرة؟
1. الدالة GetAge اتضافت لـ Person كأنها كانت جزء من الكلاس الأصلي
1. كل اللي عملناه إننا قلنا للدالة: "إنتي بتشتغلي على النوع Person" باستخدام this Person


## طيب نعمل حاجة أصعب؟

لو عايز تضيف طريقة لـ List<int> عشان تطلع المتوسط، هتكتب حاجة شبه دي:
```csharp
public static class ListExtensions
{
    public static double GetAverage(this List<int> numbers)
    {
        if (numbers == null || numbers.Count == 0)
            throw new InvalidOperationException("The list is empty or null.");

        return numbers.Average();
    }
}

```
واستخدامها يكون كده:
```csharp
List<int> numbers = new List<int> { 10, 20, 30, 40 };
double average = numbers.GetAverage();
Console.WriteLine($"The average is: {average}");
```
# العلاقة بين LINQ و Extension Methods

## ايه هو LINQ؟
- ال LINQ هو طريقة بتخليك تتعامل مع البيانات بشكل استعلامي، زي SQL، لكن جوه الكود بتاعك.
- من خلال LINQ، تقدر تكتب استعلامات في الكود بشكل مرن وواضح. زي ما تستخدم SQL في قواعد البيانات، تقدر تستخدم LINQ للاستعلام عن البيانات في C# بكل سهولة.


## العلاقة بين LINQ و Extension Methods

أكتر حاجة ملفتة في LINQ هي إنها بتستخدم **Extension Methods** عشان توفر لك دوال زي `Where`, `Select`, `OrderBy`, وغيرها. الفكرة إن LINQ ما هو إلا مجموعة من الـ Extension Methods المضافة لأنواع معينة مثل `IEnumerable<T>`، وبالتالي تقدر تستخدمها مع أي مجموعة بيانات تدعم `IEnumerable<T>`.

### مثال عملي على LINQ باستخدام Extension Methods



لما بتكتب كود LINQ زي ده:
```csharp
List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };
var evenNumbers = numbers.Where(n => n % 2 == 0).ToList();
```
- الحقيقة اللي بتحصل هي إن Where و ToList هما Extension Methods متضافين على الـ IEnumerable<T>.



## إزاي ده شغال؟
لو بصيت على تعريف الدالة Where، هتلاقيها في مكتبة LINQ بالشكل ده:
```csharp
public static IEnumerable<T> Where<T>(this IEnumerable<T> source, Func<T, bool> predicate)
{
    // Implementation هنا
}
```
 ال <this IEnumerable<T: ده بيقول إن Where ممكن تشتغل على أي حاجة بتدعم النوع IEnumerable<T>.

 ال <Func<T, bool: دي طريقة بتاخد عنصر وتحدد إذا كان بيمرر الشرط ولا لأ.

## ببساطة:
ال LINQ بيعتمد اعتماد كبير على Extension Methods عشان يوفر المرونة والسهولة دي.
من غير الـ Extension Methods، كنت هتحتاج تكتب دوال معقدة لكل عملية، لكن LINQ خلاها سهلة وبسيطة جدًا.

الملحوظة الوحيدة: خلي بالك، الـ Extension Methods مش بتعدل على الكلاس فعليًا. دي بس بتضيف طريقة جديدة بتبان كأنها جزء منه.

استخدامها بحكمة: متحولش تضيف دوال كتير لأن ده ممكن يعقد الكود ويخليه صعب في القراءة.

