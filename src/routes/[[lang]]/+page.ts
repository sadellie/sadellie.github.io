// since there's no dynamic data here, we can prerender
// it so that it gets served as a static asset in production
export const prerender = true;

import type { PageLoad } from "./$types";

export const load: PageLoad = ({ params }) => {
  interface Labels {
    name: string;
    hero: string;
    heroAction: string;
    aboutTitle: string;
    aboutBody: string;
    aboutBodySecondary: string;
    systemAnalystTitle: string;
    systemAnalystDocumentation: string;
    businessAnalystTitle: string;
    businessAnalystMarketAnalysis: string;
    businessAnalystProjectManagement: string;
    designerTitle: string;
    developerTitle: string;
    developerMobile: string;
    developerWeb: string;
    developerDesktop: string;
    successfulProjects: string;
    indexxoBody: string;
    sukkoBody: string;
    unittoBody: string;
    sadbotBody: string;
    webIdiotTitle: string;
    webIdiotBody: string;
    webPersonalTitle: string;
    webPersonalBody: string;
    commercialProjectsTitle: string;
    commercialProjectsBody: string;
    failedProductTitle: string;
    failedProductBody: string;
    contactMe: string;
  }
  const greetings: Record<string, Labels> = {
    en: {
      name: "Elshan Agaev",
      hero: "young IT specialist",
      heroAction: "Hire me!",
      aboutTitle: "Need an IT expert?",
      aboutBody: "Hello, my name is Elshan Agaev. I am an experienced:",
      aboutBodySecondary:
        "These are not all my skills, I am constantly learning something new!",
      systemAnalystTitle: "🤓 System analyst",
      systemAnalystDocumentation: "Documentation",
      businessAnalystTitle: "🤑 Business analyst",
      businessAnalystMarketAnalysis: "Market analysis",
      businessAnalystProjectManagement: "Project management",
      designerTitle: "🎨 Designer",
      developerTitle: "💻 Developer",
      developerMobile: "Mobile",
      developerWeb: "Web",
      developerDesktop: "Desktop",
      successfulProjects: "Successful projects",
      indexxoBody: "File indexer for humans",
      sukkoBody: "Create and share custom Android widgets",
      unittoBody: "Superior calculator and unit converter",
      sadbotBody: "Chatbot for students",
      webIdiotTitle: 'Web for "out of context"',
      webIdiotBody: "Made a website for my indian-based client Neha Prasad",
      webPersonalTitle: "Web for myself",
      webPersonalBody: "This and other pages were designed and developed by me",
      commercialProjectsTitle: "Commercial projects",
      commercialProjectsBody:
        "I have experience in big and cool commercial projects. Contact me for more info!",
      failedProductTitle: "Failed products",
      failedProductBody: "This list is empty... always",
      contactMe: "Contact me",
    },
    ru: {
      name: "Эльшан Агаев",
      hero: "IT Специалист",
      heroAction: "Наймите меня!",
      aboutTitle: "Нужен эксперт в области IT?",
      aboutBody: "Привет, меня зовут Эльшан Агаев:",
      aboutBodySecondary:
        "Это не все мои навыки, я постоянно изучаю что-то новое!",
      systemAnalystTitle: "🤓 Системный аналитик",
      systemAnalystDocumentation: "Документация",
      businessAnalystTitle: "🤑 Бизнес аналитик",
      businessAnalystMarketAnalysis: "Анализ рынка",
      businessAnalystProjectManagement: "Управление проектами",
      designerTitle: "🎨 Дизайнер",
      developerTitle: "💻 Разработчик",
      developerMobile: "Мобильные устройства",
      developerWeb: "Веб",
      developerDesktop: "Десктоп",
      successfulProjects: "Успешные продукты",
      indexxoBody: "Файловый индексатор для людей",
      sukkoBody: "Создавай и делись кастомными Android виджетами",
      unittoBody: "Превосходный калькулятор и перевод величин",
      sadbotBody: "Чатбот для студентов",
      webIdiotTitle: 'Веб для "out of context"',
      webIdiotBody: "Сделал вебсайт для индийского клиента Neha Prasad",
      webPersonalTitle: "Веб для своих проектов",
      webPersonalBody: "Эта и другие страницы были полностью сделаны мной",
      commercialProjectsTitle: "Коммерческие проекты",
      commercialProjectsBody:
        "У меня есть опыт в больших и крутых коммерческих проектах. Свяжитесь со мной, если хотите узнать больше!",
      failedProductTitle: "Неудачные продукты",
      failedProductBody: "Этот список пуст... всегда",
      contactMe: "Свяжитесь со мной",
    },
  };

  const lang = params.lang ?? navigator.language.toLowerCase();
  const labels = greetings[lang] ?? greetings["en"];

  return {
    labels,
  };
};
