#!/usr/bin/env python

import transmissionrpc

client = transmissionrpc.Client('127.0.0.1', port=9091)
torrents = client.info()
totDownload = 0
totUpload = 0
for tid, torrent in torrents.iteritems():
    #print('%s: %s %s %.2f%% %d %d' % (torrent.hashString, torrent.name, torrent.status, torrent.progress, torrent.rateDownload, torrent.rateUpload))
    totDownload = totDownload + int(torrent.rateDownload)
    totUpload = totUpload + int(torrent.rateUpload)

print('%d,%d' % (totUpload, totDownload))
