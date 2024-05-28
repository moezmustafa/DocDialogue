# Accessibility and WCAG

Date: June 15, 2021
Tags: design methos

In the course video, you started to learn about some of the ways that UX designers can create web pages with accessibility in mind. As a refresher, you should follow the **Web Content Accessibility Guidelines** (WCAG), which explain how to make web content more accessible to people with disabilities. You can explore [WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/) on your own to better understand the design standards recommended. To help you get started, get ready to explore a few ways to make designs more accessible.

## Accessible markup

There are several ways to mark up your designs to make them accessible for users. Here are some more details about the three methods of markup that were introduced in the video.

### Navigation order annotations

As a reminder, **annotations** are markers placed next to interactive UI elements, like call-to-action buttons, that demonstrate how people using assistive technology will navigate the app or website. In other words, annotations set the order in which a user would tab through items on a website if they use a screen reader or if they use a keyboard, instead of a touchscreen or a mouse.

Typically, the navigation order of an app or website starts from the upper-left of the screen to the lower-right. This is also called traversal order.  It is especially critical to annotate any interactive elements that fall outside of this standard navigation order, or if the user’s initial focus should stray from the first interactive element placed in the upper left of the screen.

You can use numbers to illustrate the number of key presses, or tabs, from one item to the next. These numbers are shown in green circles in the image below. When the product is in development, engineers use these annotations too, to clarify any modifications to the standard navigation order.

![https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/nluJIMiHRxWbiSDIh3cV5Q_75ccfe4ce2fd41daa392fbf5e16b5f3a_Learn-more-about-web-accessibility-1.svg?expiry=1623888000000&hmac=U4fHOzS8pO75SmaUIGMxCPFzJK6wb6lYGlK8s3ScV5U](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/nluJIMiHRxWbiSDIh3cV5Q_75ccfe4ce2fd41daa392fbf5e16b5f3a_Learn-more-about-web-accessibility-1.svg?expiry=1623888000000&hmac=U4fHOzS8pO75SmaUIGMxCPFzJK6wb6lYGlK8s3ScV5U)

### Hierarchical headings

As you learned earlier in the certificate program, **hierarchy** is a visual design principle that designers use to order elements on a page and classify them by their level of importance.

**Headings** are named sections of a page that use different font sizes, which are larger than the body font size. You can use headings to show hierarchy in your designs and help users easily navigate the page.

Headings are written in **HTML**, the language of the internet. Having specific heading tags, like H1, H2, and H3, allows screen readers to interpret the hierarchy of a page for users. The H1 tag indicates that a particular heading is the most important on the page and is often used for titles. An H2 tag is used for subtitles or callout boxes. Additional tags, like H3, can also be used to further indicate the hierarchy of the page. The image below shows a wireframe of a website with heading tags.

![https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/8HNT2zZURJOzU9s2VMSTfQ_ccb2f026571142b293fc089c6be6dbb4_Learn-more-about-web-accessibility-2.svg?expiry=1623888000000&hmac=jR-mtpfX8AdS02FIiFxEmAr2f9LalVCMZNsJWJ1tw58](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/8HNT2zZURJOzU9s2VMSTfQ_ccb2f026571142b293fc089c6be6dbb4_Learn-more-about-web-accessibility-2.svg?expiry=1623888000000&hmac=jR-mtpfX8AdS02FIiFxEmAr2f9LalVCMZNsJWJ1tw58)

### Accessibility labels

**Labels**, or screen reader verbalizations, add descriptive language to the interactive UI elements on the web page. With a label, there can be no doubt about the purpose of the button, menu, or checkbox. For example, a label might read “When the user clicks the checkbox, select the item.” Check out additional examples of labels that a screen reader should read aloud for each button in the image below.

When annotating labels for interactive elements on your web site designs, note where similar controls should be grouped to provide more efficiency and context. For example, consider grouping a list of checkboxes so that a user of assistive technology could understand the relationship of the checkboxes and how to quickly navigate to and from them.

Engineers use these labels to determine the best implementation for the experience you are trying to accomplish.

![https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/xpAnryd5SgiQJ68neSoIRQ_acb0f0de980848648a57533023704abe_Learn-more-about-web-accessibility-4.svg?expiry=1623888000000&hmac=MvksIrBRMbXtdjckbuX_1uKOQQ0ilPOFvHLs7mEcurw](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/xpAnryd5SgiQJ68neSoIRQ_acb0f0de980848648a57533023704abe_Learn-more-about-web-accessibility-4.svg?expiry=1623888000000&hmac=MvksIrBRMbXtdjckbuX_1uKOQQ0ilPOFvHLs7mEcurw)

To keep learning, check out an article from Adobe XD about [annotating your design work](https://xd.adobe.com/ideas/process/wireframing/benefits-of-annotating-wireframes/) and an article from WebAIM that provides [an introduction to Accessible Rich Internet Applications (ARIA)](https://webaim.org/techniques/aria/).

## Accessible color and contrast

In an earlier course of the certificate program, you learned how to implement color and contrast to ensure they align with accessibility guidelines. Remember learning the term **luminosity contrast ratio**? ****It’s a measurement of the contrast between the background of a design and the text color used with it. In short, your designs will be more accessible if you choose a light background with a dark text, or a dark background with a light text.

Additionally, you need to carefully consider the color combinations you choose for your designs. People who are colorblind may experience difficulties differentiating between certain color combinations, like red-green. Plus, many people, especially those who have low contrast sensitivity, may not be able to distinguish individual shapes if the color combinations are too similar, like light gray and white. When choosing colors, reference the [WebAIM contrast and color requirements](https://webaim.org/articles/contrast/) to ensure your designs meet accessibility standards.

Still have questions? Revisit this reading about [accessibility considerations for color](https://www.coursera.org/learn/high-fidelity-designs-prototype/item/Ca3gb) for a refresher.

## Make responsive websites accessible

As you design a responsive website that adapts to different screen sizes, you need to make sure that all versions of your website are accessible. For example, if users zoom in on an element or increase the size of the font to meet their vision needs, the rest of the page should automatically resize and rearrange to fit the new screen size. Otherwise, when a user enlarges a section of the page, elements might overlap each other.

In the image below, notice how the screen should adapt when a user zooms in, as compared to a responsive website that does not resize — the text becomes unreadable.

![https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/eXsGAYT_TvC7BgGE_x7wMQ_033515205e554b94ade74d14e47bba2f_Learn-more-about-web-accessibility-3.svg?expiry=1623888000000&hmac=qDyMeRcNZet2m8l3tdzBW3Fr6KEAtjmgqX4US7R_H6g](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/eXsGAYT_TvC7BgGE_x7wMQ_033515205e554b94ade74d14e47bba2f_Learn-more-about-web-accessibility-3.svg?expiry=1623888000000&hmac=qDyMeRcNZet2m8l3tdzBW3Fr6KEAtjmgqX4US7R_H6g)

It’s critical to communicate these different interactions to engineers. For example, it’s helpful to create multiple versions of your mockups: one to show the designs at the default display and text settings, and another to show the enlarged (or zoomed in) display. That way, you can take magnification and other responsive design requirements into account before the website is fully developed.

## Additional resources

There’s a lot more to learn when it comes to designing accessible websites! Check out this page about [designing with accessibility in mind](https://material.io/design/usability/accessibility.html) on Google’s Material Design website, which includes guidance about hierarchy, color, layouts, and more. In addition, explore [The A11Y Project](https://www.a11yproject.com/), a collection of resources from designers across industries that was created to make digital accessibility easier.