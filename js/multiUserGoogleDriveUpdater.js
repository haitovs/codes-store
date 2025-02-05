function fetchApiData(url) {
  var response = UrlFetchApp.fetch(url);
  return response.getContentText();
}

function updateMultipleGoogleDriveFiles() {
  var files = [
    { name: 'yagmyrGLOBAL', fileId: '1Uws2kDmn8bxI7SNPMM640ZkXXAxLAJ9H', url: 'https://spikeasdf.top/sub/eWFnbXlyR0xPQkFMLDE3MjQ2NTgzMjUgExc7vZwa-'},
    { name: 'rahman', fileId: '1Wf72JMBa6NLH-mQnljS0_5UdAO6Fyci1', url: 'https://spikeasdf.online/sub/cmFobWFuLDE3MjQzNTQzNTI5wWtC8EKbg'},
    { name: 'muhammet', fileId: '1wzhiZTES3kPedi3x4pzg1BWLF7QMdfCS', url: 'https://spikeasdf.online/sub/bXVoYW1tZXQsMTcyNDM1NDM1Mgc_LcywBBKg'},
    { name: 'merdan', fileId: '14PNVygAVYiFfWOu1WjdDd5ydhEtV0etV', url: 'https://spikeasdf.top/sub/bWVyZGFuLDE3MjQ2NTgzMjUY-gHGMvq3O'},
    { name: 'mammet', fileId: '1rSbtyxLMMQHKFi0tHz-t65kBM-aWqCLQ', url: 'https://spikeasdf.online/sub/bWFtbWV0LDE3MjQzNTQzNTINGVJznXQvm'},
    { name: 'hudikArslan', fileId: '1EDGess6ndDyKJ0eOdjRzpZLlUDLHL0Lc', url: 'https://spikeasdf.online/sub/aHVkaWtBcnNsYW4sMTcyNDUzMzgxMANcksadHY2g'},
    { name: 'halkberdiKl', fileId: '16KU0U9TB9iM3zQQccpLOF2waAe551viE', url: 'https://spikeasdf.top/sub/aGFsa2JlcmRpS2wsMTcyNDY1NDIzNwqiVbrKYt96'},
    { name: 'gadam', fileId: '1kmX4Pa23NchM-VJ5hHi-PIXV0cbNxU5S', url: 'https://spikeasdf.online/sub/Z2FkYW0sMTcyNDYzMTg1NQp31Clb2h9y'},
    { name: 'azatDwor', fileId: '1S5jEMpDWi7ags_tJrybwH4InAUShJi_B', url: 'https://spikeasdf.online/sub/YXphdER3b3IsMTcyNDM1NDM1MgvPqCRUKQwv'},
    { name: 'aryf', fileId: '1MPVTxhKMKMX8df2GcUI14_PObKpiuXHT', url: 'https://spikeasdf.online/sub/YXJ5ZiwxNzI0NTI1Mjg4kiCzX28u36'},
    { name: 'arslanStarshiy', fileId: '1r8jDKhy6AZiSaZ_9h5MJnCNs4DhR5gR9', url: 'https://spikeasdf.online/sub/YXJzbGFuU3RhcnNoaXksMTcyNDM1NDM1MgToSqdQ83UJ'},
    { name: 'arslanKurs', fileId: '1UuK998IsN__9knvfZ6kFMGfCR9EauTYf', url: 'https://spikeasdf.online/sub/YXJzbGFuS3VycywxNzI0MzU0MzUyPrm-Z1WJpj'},
    // Add more name, fileId, and url pairs here
  ];

  files.forEach(function(fileInfo) {
    var file = DriveApp.getFileById(fileInfo.fileId);
    var text = fetchApiData(fileInfo.url);
    
    if (text) {
      file.setContent(text);
    }

    // Log information for your reference (optional)
    Logger.log('Updated file for: ' + fileInfo.name);
  });
}

function setUpTriggerForMultipleUpdates() {
  // Run the update function immediately upon setting the trigger
  updateMultipleGoogleDriveFiles();
  
  // Check for existing trigger and remove it if found
  var triggers = ScriptApp.getProjectTriggers();
  for (var i = 0; i < triggers.length; i++) {
    if (triggers[i].getHandlerFunction() == 'updateMultipleGoogleDriveFiles') {
      ScriptApp.deleteTrigger(triggers[i]);
    }
  }

  // Create a new trigger to run the update function every 5 minutes
  ScriptApp.newTrigger('updateMultipleGoogleDriveFiles')
    .timeBased()
    .everyMinutes(5)
    .create();
}
