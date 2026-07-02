:orphan:

.. _doc_hosting_servers_using_private_workshop_files:

Hosting Servers Using Private Workshop Files
============================================

Unfortunately, the dedicated server cannot login to a Steam account to download private workshop files. So, a workaround is necessary.

By logging into steamcmd you can download the workshop file using your account:

  #. ``login (credentials)``
  #. ``workshop_download_item 304930 (workshopfileid)``

This will download the file into the steamcmd folder at ``steamapps/workshop/content/304930/(workshopfileid)``.

You can now create a symbolic link between the server and the workshop file.
For example on Linux testing map ``MyMap``, open the U3DS folder and use:

``ln -S ../../workshop/content/304930/(workshopfileid)/MyMap Maps/MyMap``

The workshop file ID should still be added to ``WorkshopDownloadConfig.json`` so that clients enable it when joining.
