
# AirBnB clone - Web static

## Background Context
Web static, what?

Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!

Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:

    Create simple HTML static pages
    Style guide
    Fake contents
    No Javascript
    No data loaded from anything

During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

Before starting, please fork or clone the repository AirBnB_clone from your partner if you were not the owner of the previous project.

***
## General

### What is HTML

### How to create an HTML page

### What is a markup language
A markup language is a system for annotating or tagging text in order to define its structure, presentation, or behavior. It uses tags or elements to indicate how the text should be displayed or processed. The tags are embedded within the text and provide instructions to software or browsers on how to interpret and render the content.

### What is the DOM
The DOM stands for Document Object Model. It is a programming interface that represents the structure of an HTML or XML document as a tree-like structure, where each node in the tree represents an element, attribute, or piece of text in the document.

The DOM provides a way for programs or scripts to dynamically access and manipulate the content, structure, and style of a web page or XML document. It essentially serves as an application programming interface (API) between the web page and the scripting language (such as JavaScript) running in a web browser.

### What is an element / tag
An element (also referred to as a tag) is a fundamental building block used to define the structure and content of a document. Elements are represented by tags enclosed in angle brackets (< >) and can be nested within each other to form a hierarchical structure.

Elements define the structure and semantics of a document. They represent different types of content, such as headings, paragraphs, links, images, tables, lists, and more.

### What is an attribute
Elements can also have attributes, which provide additional information about the element. Attributes are specified within the start tag and consist of a name-value pair. For example, in `<a href="https://example.com">`, href is the attribute name, and `"https://example.com"` is the attribute value.

### How does the browser load a webpage
Parsing the HTML: The browser starts by fetching the HTML document specified by the URL. It then parses the HTML code from top to bottom, constructing the Document Object Model (DOM) tree. During this process, the browser identifies elements, tags, attributes, and their relationships to form the structure of the webpage.

Fetching external resources: While parsing the HTML, the browser encounters external resources referenced in the document, such as CSS stylesheets, JavaScript files, images, and other media files. It starts fetching these resources in parallel to avoid delays.

Constructing the CSSOM: As the browser fetches CSS stylesheets, it simultaneously parses them to create the CSS Object Model (CSSOM). The CSSOM represents the styles applied to elements in the DOM tree.

Rendering the webpage: Once the DOM tree and CSSOM are constructed, the browser combines them to create the render tree. The render tree contains only the elements and styles necessary to display the webpage. It excludes elements that are hidden or not relevant to the current view, such as those inside `<head>` or hidden by CSS rules.

### What is CSS
### How to add style to an element
CSS allows you to control the presentation and appearance of elements on a webpage.
>
Internal Stylesheet: You can define styles within the `<style>` tag in the head section of your HTML document. The styles specified inside the `<style>` tag will apply to the elements on that page.

External Stylesheet: You can create a separate CSS file with the .css extension and link it to your HTML document using the `<link>` tag. This approach allows you to define styles in a separate file and apply them to multiple HTML pages.
### What is a class
In the context of HTML and CSS, a class is a way to assign a specific name to one or more elements on a webpage. It allows you to apply common styles or behaviors to multiple elements without having to repeat the styles for each individual element.
>
To define a class for an element, you use the class attribute. The class attribute can be added to any HTML element and accepts a space-separated list of class names.

>```<p class="highlight">This is a paragraph with a class.</p>```

In the above example, the paragraph element (`<p>`) has a class assigned to it. The class name is "highlight". You can name your classes according to their purpose or the styles they represent.

>.highlight {
>
>  color: red;
>
>  font-weight: bold;
>
> }
>
In the CSS code above, the .highlight class selector targets elements with the "highlight" class. The specified styles (red text color and bold font weight) will be applied to any element that has the "highlight" class.

### What is a selector
In CSS, a selector is a pattern that identifies one or more HTML elements to which a set of styles should be applied. Selectors determine which elements in an HTML document will be targeted and styled using CSS rules.

### How to compute CSS Specificity Value
CSS specificity is a value assigned to a selector that determines which styles will be applied to an element when there are conflicting styles from multiple selectors. Specificity is calculated based on the components of a selector and helps establish the order of precedence for applying styles.

To compute the specificity value, you can follow these rules:

    Start with a specificity value of 0, 0, 0, 0.

    Add 0, 0, 1, 0 for each style rule containing an ID selector.

    Add 0, 1, 0, 0 for each style rule containing a class selector, attribute selector, or pseudo-class selector.

    Add 1, 0, 0, 0 for each style rule containing an element selector or pseudo-element selector.

    For each part of a selector, repeat steps 2-4 and accumulate the specificity values.

    If there is a tie, the most recently declared style takes precedence.
### What are Box properties in CSS
In CSS, box properties refer to a set of CSS properties that control the dimensions, layout, and appearance of elements on a webpage. These properties affect how elements are displayed and positioned within their containing box.
