{
	"targets": [
		{
			"target_name": "keylistener",
			"type": "executable",
			"xcode_settings": {
              "OTHER_LDFLAGS": [
    			'-mmacosx-version-min=10.7',
				'-framework', 'Foundation',
				'-framework', 'CoreData',
				'-framework', 'Cocoa',
				'-framework', 'Carbon',
				'-fno-objc-arc',
			  ],
			},
			"sources": [
				"FMMediaKeyDelegate.m",
				"main.m",
				"SPMediaKeyTap.m",
				"StdinListener.m"
			]
		}
	]
}
