function smartEmailLabeler() {
  const threads = GmailApp.getInboxThreads(0, 50); // latest 50 threads

  const iitbLabel = GmailApp.createLabel("IITB");
  const externalLabel = GmailApp.createLabel("External");

  const subclassLabels = {
    "Tech Application": ["tech team", "recruitment", "application", "join us", "openings"],
    "Competition": ["Techfest", "Mood Indigo", "competition", "hackathon", "contest", "challenge"],
    "Lecture/Academics": ["lecture", "course", "quiz", "assignment", "class", "syllabus"],
    "Interview Call": ["interview", "shortlisted", "HR", "round", "selection", "offer"],
    "Meeting": ["meeting", "invite", "calendar", "zoom", "google meet"]
  };

  threads.forEach(thread => {
    const messages = thread.getMessages();
    const msg = messages[messages.length - 1]; // latest message in thread
    const sender = msg.getFrom().toLowerCase();
    const subject = msg.getSubject().toLowerCase();
    const body = msg.getPlainBody().toLowerCase();

    const isIITB = sender.includes("@iitb.ac.in");

    const parentLabel = isIITB ? iitbLabel : externalLabel;
    thread.addLabel(parentLabel);

    for (let category in subclassLabels) {
      const keywords = subclassLabels[category];
      if (keywords.some(word => subject.includes(word) || body.includes(word))) {
        const subLabel = GmailApp.createLabel(`${isIITB ? "IITB" : "External"}/${category}`);
        thread.addLabel(subLabel);
      }
    }
  });
}
